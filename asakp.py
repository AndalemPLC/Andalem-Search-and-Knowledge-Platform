from configparser import ConfigParser
from googlesearch import search
import gradio as gr
from langchain_community.llms import ollama
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from misc_resources.styles import Styles
from misc_resources.theme import Theme
from utilities.search_logger import SearchLogger
from utilities.system_logger import SystemLogger

configuration = ConfigParser()
configuration_file = './config.ini'
configuration.read(configuration_file)
app_name = configuration.get('app_details', 'app_name')
app_version = configuration.get('app_details', 'app_version')
app_copyright = configuration.get('app_details', 'app_copyright')

styles = Styles.styles
theme = Theme.theme

mode_setter = f"""
                   window.onload = function() {{
                        
                      document.body.classList.remove('light');
                      document.body.classList.add('dark');

                   }}
               """

ollama_base_url = 'https://a40e-196-188-245-26.ngrok-free.app'
timeout = 100

def evaluate_relevance_with_llm(query, url):

  llm = ollama.Ollama(model = 'llama3', temperature = 0, top_p = 0.7, base_url = ollama_base_url, timeout = timeout)
  
  prompt = f"Query: {query}\nDocument: {url}\nHow relevant is this URL's content to the query on a scale of 1 to 10?"

  llm_result = llm.invoke(prompt)
  
  relevance_score = extract_relevance_score(llm_result.content)
  
  return relevance_score

def extract_relevance_score(response):

  relevance_score = [int(s) for s in response.split() if s.isdigit()]
  
  return relevance_score[0] if relevance_score else 0

def process_query(query):

  results = []
    
  search_results = search(query, num_results = 10, safe = 'active', sleep_interval = 5, timeout = 25, advanced = True)

  for idx, result in enumerate(search_results, 1):
    
    results.append({'google_rank': idx,
                    'url': result.url,
                    'title': result.title,
                    'description': result.description})
    
  print(results)
  
  if len(results) == 0:
      
    return 'No relevant results found for the given query!'
  
  else:
      
    print(f"{len(results)} relevant results found for the given query!")

  return results

def generate_search_results_content(urls, query, task):

  llm = ollama.Ollama(model = 'llama3', temperature = 0, top_p = 0.7, base_url = ollama_base_url, timeout = timeout)

  if task == 'summary':

    prompt = f"""You are tasked with writing a detailed summary that answers the following query based on 
    the content found on multiple webpages:

    '{query}'

    Using information from the following URLs:
    {', '.join([f"- {url}" for url in urls])}

    Your goal is to provide a comprehensive, in-depth response to the query, synthesizing key insights and 
    details from all the provided webpages. Ensure the response is informative, well-structured, and formatted 
    in HTML for display purposes. 

    Structure the response into clear sections and use paragraph tags (<p>, </p>) for blocks of text. 
    Additionally, include citations in the summary, clearly indicating the source URL for each important point 
    or piece of information by linking to the original page like this:

    <a href="{urls[0]}" target="_blank">[Source]</a>

    Focus on producing a thoughtful, well-supported answer, and ensure that your response remains factual and 
    relevant to the query.
    """

    error_message = 'There was an error performing summary generation! Check the log for details.'
  
  elif task == 'excerpt':

    excerpt_length = 200
    
    prompt = f"""You are tasked with analyzing the content of the webpage found at '{urls[0]}'.
    Please summarize the webpage in a concise, at-a-glance format (Of around {excerpt_length} words) that 
    addresses or answers the following query:

    '{query}'

    Ensure the response is informative and directly relevant to the query. Format the output as HTML for display 
    purposes, using paragraph tags (<p>, </p>) for text blocks, and include a clickable link to the original 
    page using the following format:

    <a href="{urls[0]}" target="_blank">Read More</a>

    Keep the summary factual and extract key insights from the content of the webpage.
    """   

    error_message = 'There was an error performing excerpt extraction! Check the log for details.'

  elif task == 'related_queries':

    output_parser = CommaSeparatedListOutputParser()
    
    format_instructions = output_parser.get_format_instructions()

    prompt_template = PromptTemplate(template = """Based on the following query and the content of these 
                                     webpages, generate four related questions that the user might also want 
                                     to ask or explore in relation to this topic. The questions should be 
                                     informative and guide the user to further areas of interest.
                                     Return **only** the four questions, without any explanations.
                                     
                                     User's query: '{query}'
                                     
                                     URLs: {urls}
                                     
                                     The related questions should reflect potential follow-up inquiries or 
                                     other important topics the user might want to know about.
                                     
                                     {format_instructions}
                                     """, 
                                     input_variables = ['query', 'urls'], 
                                     partial_variables = {'format_instructions': format_instructions})
    
    prompt = prompt_template.format(query = query, urls = '\n'.join([f"- {url}" for url in urls]))

    error_message = 'There was an error generating related queries! Check the log for details.'

  try:
    
    result = llm.invoke(prompt)
    
    if task == 'related_queries':
        
      chain = prompt_template | llm | output_parser

      related_queries = chain.invoke({'query': query, 'urls': '\n'.join([f"- {url}" for url in urls])})

      return related_queries
    
    print(result)
    
    return result

  except Exception as exception:
      
    SystemLogger.system_logger.error(f'There was an error during {task} generation: {str(exception)}')
      
    raise gr.Error(error_message)

def set_search_query(search_query):

  return gr.Textbox(search_query[0])

def search_and_rank(query):

  results = process_query(query)

  if isinstance(results, str):
      
    no_results_message = 'No relevant results found for the given query!'

    return (no_results_message, no_results_message, gr.Dataset(samples = [['Related Query 1'], ['Related Query 2'], ['Related Query 3'], ['Related Query 4']], visible = False))

  else:
  
    urls = [result['url'] for result in results]
    
    summary = generate_search_results_content(urls, query, 'summary')

    summary = f"""<div class="overall-summary">{summary}</div>"""
    
    results_list = ''

    for index, result in enumerate(results):

      excerpt = generate_search_results_content([result['url']], query, 'excerpt')

      results_list += f"""<div class="search-result">
      <h3 class="title">{result['title']}</h3>
      <p class="description">{result['description']}</p>
      <p class="excerpt">{excerpt}</p>
      <p class="rank-relevance"><b>Google Rank:</b> {result['google_rank']:.2f}<p>
      </div>"""

    related_queries = generate_search_results_content(urls, query, 'related_queries')

    SearchLogger.log_search(query, results, summary, results_list, related_queries)

    return (summary, results_list, gr.Dataset(samples = [[query.strip()] for query in related_queries], visible = True))

with gr.Blocks(title = app_name,
               theme = theme,
               css = styles,
               js = mode_setter,
               fill_height = True) as asakp:
    
  with gr.Row(elem_id = 'header-row'):

    with gr.Column():

      with gr.Row():

        app_logo = gr.Image(elem_id = 'app-logo-container',
                            value = './app_images/andalem-logo-with-motto.png',
                            show_download_button = False,
                            show_share_button = False, 
                            container = False,
                            interactive = False,
                            show_fullscreen_button = False,
                            key = 'app_logo')

  with gr.Row(elem_id = 'search-text-box-row'):

    with gr.Column(elem_id = 'search-text-box-column', scale = 1, min_width = 300):

      search_text_box = gr.Textbox(elem_id = 'search-text-box-container',
                                   label = 'Search Text Box:',
                                   show_label = False, 
                                   value = '',
                                   placeholder = 'Enter your search query . . .',
                                   interactive = True,
                                   lines = 1,
                                   max_lines = 1,
                                   container = False,
                                   submit_btn = True,
                                   key = 'search_text_box')
      
  search_results_summary_row = gr.Row(elem_id = 'search-results-summary-row', show_progress = True, visible = True)

  with search_results_summary_row:

    search_results_summary = gr.HTML(elem_id = 'search-results-summary-container',
                                     label = 'Search Results Summary',
                                     show_label = False,
                                     key = 'search_results_summary')
      
  search_results_list_row = gr.Row(elem_id = 'search-results-list-row', show_progress = True, visible = True)
        
  with search_results_list_row:
          
    search_results_list = gr.HTML(elem_id = 'search-results-list-container',
                                  label = 'Search Results List',
                                  show_label = False,
                                  key = 'search_results_list')
      
  related_queries_row = gr.Row(elem_id = 'related-queries-row', show_progress = True, visible = True)

  with related_queries_row:

    related_queries_component_textbox = gr.Textbox(elem_id = 'related-queries-component-textbox-container',
                                                   label = 'Related Queries Component Textbox:',
                                                   show_label = False, 
                                                   value = '',
                                                   interactive = False,
                                                   lines = 1,
                                                   max_lines = 5,
                                                   container = False,
                                                   visible = False,
                                                   key = 'related_queries_component_textbox') 
    
    related_queries = gr.Dataset(elem_id = 'related-queries-container',
                                 label = 'Related Queries',
                                 samples = [['Related Query 1'],
                                            ['Related Query 2'],
                                            ['Related Query 3'],
                                            ['Related Query 4']],
                                 components = [related_queries_component_textbox],
                                 container = False,
                                 visible = False,
                                 key = 'related_queries')

  search_text_box.submit(search_and_rank, 
                         inputs = [search_text_box],
                         outputs = [search_results_summary, search_results_list, related_queries])
  
  related_queries.click(set_search_query, 
                        inputs = [related_queries],
                        outputs = [search_text_box], 
                        scroll_to_output = True).then(search_and_rank, 
                                                      inputs = [search_text_box],
                                                      outputs = [search_results_summary, search_results_list, related_queries])

  with gr.Row(elem_id = 'footer-row'):

      gr.Markdown(f'<p>{app_copyright}</p>', elem_id = 'footer-text-container')                                                

if __name__ == '__main__': 

  asakp.queue(default_concurrency_limit = 100)

  asakp.launch(favicon_path = './app_images/andalem-icon.png',
               inbrowser = True,
               show_api = False, 
               show_error = False,
               share = False,
               server_name = '127.0.0.1',
               server_port = 7860)