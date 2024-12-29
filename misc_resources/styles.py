class Styles:

    styles = """
                 :root {
                    --main-area-height: calc(100vh - 110px);
                    --logo-color: #D22C2E;
                    --error-color: #901214;
                    --info-color: #154678;
                    --success-color: #085409;
                    --warning-color: #8B7A10;
                 }

                 .gradio-container {
                    max-width: 100% !important;
                    
                 }

                 .fill-main-area-height {
                    max-height: var(--main-area-height);
                 }

                 .scrollable {
                    overflow-y: auto;
                 }

                 *::-webkit-scrollbar {
                    width: 5px;
                 }

                 *::-webkit-scrollbar-track {
                    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
                    border-radius: 10px;
                    -webkit-border-radius: 10px;
                 }

                 *::-webkit-scrollbar-thumb {
                    background: var(--logo-color); 
                    border-radius: 10px;
                    -webkit-border-radius: 10px;
                    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.5); 
                 }

                 *::-webkit-scrollbar-button {
                    display: none !important;
                 }

                 *::-webkit-scrollbar-corner {
                    background: var(--body-background-fill);
                    border-radius: 10px;
                    -webkit-border-radius: 10px;
                 }

                 *::-webkit-resizer {
                    display: none;
                 }

                 #header-row .image-container {
                    cursor: default !important;
                    margin-bottom: 20px;
                 }
            
                 #app-logo-container img { 
                    text-align: center;   
                    display: block;
                    margin-left: auto;
                    margin-right: auto;                            
                    width: 200px;
                    cursor: default !important;
                 }

                 #search-text-box-container {
                    width: 50%;
                    margin-left: auto;
                    margin-right: auto;
                 }

                #search-text-box-container.block.svelte-5y6bt2 {
                    background: var(--input-background-fill);
                }

                #search-text-box-container .submit-button {
                    color: var(--body-text-color);
                    margin-top: 5px;
                    margin-right: 5px;
                    margin-bottom: 5px;
                    background: var(--logo-color);
                }

                #search-text-box-container .submit-button:hover {
                    background: var(--body-background-fill);
                }

                .pending.svelte-1gpwetz {
                    background: var(--body-background-fill) !important;
                }

                 .overall-summary {
                    background: var(--background-fill-primary);
                    border: 1px solid var(--border-color-primary);
                    border-radius: 7px;   
                    padding: 20px;  
                    margin-top: 20px;
                    margin-bottom: 10px !important;             
                 }

                 .overall-summary a {
                    color: var(--logo-color);
                    text-decoration: none;
                    font-weight: bold;
                 }

                 .overall-summary a:hover {
                    color: var(--body-text-color);
                 }

                 .search-result {
                    background: var(--background-fill-primary);
                    border: 1px solid var(--border-color-primary);
                    border-radius: 7px; 
                    padding: 20px;
                    margin-bottom: 20px;
                 }

                 .title {
                    margin-bottom: 10px;
                 }

                 .description {
                    font-style: italic;
                    margin-bottom: 10px;
                 }

                 .excerpt {
                    margin-top: 10px;
                    margin-bottom: 10px;
                 }

                 .rank-relevance, .score-similarity {
                    margin-top: 10px;
                 }

                 .search-result a {
                    color: var(--logo-color);
                    text-decoration: none;
                    font-weight: bold;
                 }

                 .search-result a:hover {
                    color: var(--body-text-color);
                 }

                 #related-queries-row {
                    width: 50%;
                    margin-top: 10px;
                 }

                 #related-queries-container svg {
                    display: none;
                 }

                 #related-queries-container .label {
                    font-size: 18px;
                    margin-top: 5px !important;
                    margin-bottom: 20px !important;
                 }

                 #related-queries-container button {
                    color: var(--body-text-color);
                    background: var(--body-background-fill);
                    border: 1px solid var(--body-text-color);
                    text-align: center;
                    width: 100%;
                    padding: 10px;
                 }

                 #related-queries-container button:hover {
                    color: var(--logo-color);
                    background: var(--body-background-fill);
                    border: 1px solid var(--logo-color);
                    padding: 10px;
                 }

                 .form {
                    background: none !important;
                    border: 0px !important;
                 }

                 textarea {
                    resize: none;
                 }

                 #footer-row {
                    display: flex;
                    margin-top: auto;
                 }

                 #footer-text-container p {
                    font-size: 14px;                            
                    font-weight: normal;
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-top: 10px;
                    margin-right: auto;
                    margin-bottom: 10px;
                    width: 100%;
                    opacity: 0.7;
                 }

                 footer {
                    display: none !important;
                 }

                 .unset-overflow {
                    overflow: unset !important;
                 }
             """   