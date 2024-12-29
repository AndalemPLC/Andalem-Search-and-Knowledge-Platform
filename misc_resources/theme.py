import gradio as gr

class Theme:

    theme = gr.themes.Default(primary_hue = 'red', 
                              secondary_hue = 'blue').set(body_background_fill = '#EEEEEE',
                                                          body_background_fill_dark = '#0B0F19',
                                                          background_fill_primary = '#CCCCCC',
                                                          background_fill_primary_dark = '#111827',
                                                          background_fill_secondary = '#DDDDDD',
                                                          background_fill_secondary_dark = '#131720',
                                                          border_color_primary = '#1E1E1E',
                                                          border_color_primary_dark = '#727278',
                                                          body_text_color = '#1E1E1E',
                                                          body_text_color_dark = '#FFFFFF',
                                                          slider_color = '*primary_500',
                                                          slider_color_dark = '*primary_600',                                                           
                                                          shadow_drop = 'none',
                                                          shadow_drop_lg = 'none',                                                     
                                                          block_info_text_color = '#1E1E1E',
                                                          block_info_text_color_dark = '#FFFFFF',
                                                          block_label_padding = '*spacing_sm *spacing_md',
                                                          block_label_background_fill = 'none',
                                                          block_label_background_fill_dark = 'none',
                                                          block_label_radius = 'none',
                                                          block_label_text_size = '*text_md',
                                                          block_label_text_weight = '600',
                                                          block_label_text_color = '#1E1E1E',
                                                          block_label_text_color_dark = '#FFFFFF',
                                                          block_title_radius = 'none',
                                                          block_title_padding = '*block_label_padding',
                                                          block_title_background_fill = 'none',
                                                          block_title_text_weight = '600',
                                                          block_title_text_color = '#1E1E1E',
                                                          block_title_text_color_dark = '#FFFFFF',
                                                          block_label_margin = '*spacing_md',
                                                          block_border_width = '1px',
                                                          panel_border_width = '1px',                                                    
                                                          input_background_fill = '#FFFFFF',
                                                          input_background_fill_dark = '#373740',
                                                          input_background_fill_focus = '#FFFFFF',
                                                          input_background_fill_focus_dark = '#373740',
                                                          input_background_fill_hover = '#FFFFFF',
                                                          input_background_fill_hover_dark = '#373740',
                                                          input_border_color = '#1E1E1E',
                                                          input_border_color_dark = '#727278',
                                                          input_border_color_focus = '#1E1E1E',
                                                          input_border_color_focus_dark = '#727278',
                                                          input_border_color_hover = '#1E1E1E',                                                                
                                                          input_border_color_hover_dark = '#727278',
                                                          input_shadow = '*shadow_drop',
                                                          input_shadow_focus = '*shadow_drop_lg',
                                                          checkbox_background_color = '#FFFFFF',
                                                          checkbox_background_color_dark = '#373740',
                                                          checkbox_background_color_selected = '#D22C2E',
                                                          checkbox_background_color_selected_dark = '#D22C2E',
                                                          checkbox_background_color_focus = '#FFFFFF',
                                                          checkbox_background_color_focus_dark = '#373740',
                                                          checkbox_background_color_hover = '#FFFFFF',
                                                          checkbox_background_color_hover_dark = '#373740',
                                                          checkbox_shadow = 'none',
                                                          checkbox_label_background_fill_selected = 'none',
                                                          checkbox_label_background_fill_selected_dark = 'none',
                                                          checkbox_border_width = '1px',
                                                          checkbox_border_color = '#1E1E1E',
                                                          checkbox_border_color_dark = '#727278',
                                                          checkbox_border_color_focus = '#1E1E1E',
                                                          checkbox_border_color_focus_dark = '#727278',
                                                          checkbox_border_color_selected = '#1E1E1E',
                                                          checkbox_border_color_selected_dark = '#727278',
                                                          checkbox_label_text_color_selected = '#1E1E1E',
                                                          checkbox_label_text_color_selected_dark = '#FFFFFF',
                                                          shadow_spread = '6px',
                                                          checkbox_label_shadow = '*shadow_drop_lg',
                                                          button_primary_background_fill = '#CCCCCC',
                                                          button_primary_background_fill_dark = '#111827',
                                                          button_primary_background_fill_hover = '#CCCCCC',
                                                          button_primary_background_fill_hover_dark = '#111827',
                                                          button_primary_border_color = '#1E1E1E',
                                                          button_primary_border_color_dark = '#727278',
                                                          button_primary_border_color_hover = '#D22C2E',
                                                          button_primary_border_color_hover_dark = '#D22C2E',
                                                          button_primary_text_color = '#1E1E1E',
                                                          button_primary_text_color_dark = '#FFFFFF',
                                                          button_primary_text_color_hover = '#D22C2E',                                                               
                                                          button_primary_text_color_hover_dark = '#D22C2E',
                                                          button_secondary_background_fill = '#CCCCCC',
                                                          button_secondary_background_fill_dark = '#111827',
                                                          button_secondary_background_fill_hover = '#CCCCCC',
                                                          button_secondary_background_fill_hover_dark = '#111827',
                                                          button_secondary_border_color = '#1E1E1E',
                                                          button_secondary_border_color_dark = '#727278',
                                                          button_secondary_border_color_hover = '#D22C2E',
                                                          button_secondary_border_color_hover_dark = '#D22C2E',
                                                          button_secondary_text_color = '#1E1E1E',
                                                          button_secondary_text_color_dark = '#FFFFFF',
                                                          button_secondary_text_color_hover = '#D22C2E',                                                               
                                                          button_secondary_text_color_hover_dark = '#D22C2E',
                                                          button_cancel_background_fill = '#D22C2E',
                                                          button_cancel_background_fill_dark = '#D22C2E',
                                                          button_cancel_background_fill_hover = '#CCCCCC',
                                                          button_cancel_background_fill_hover_dark = '#111827',
                                                          button_cancel_border_color = '#D22C2E',
                                                          button_cancel_border_color_dark = '#D22C2E',
                                                          button_cancel_border_color_hover = '#D22C2E',
                                                          button_cancel_border_color_hover_dark = '#D22C2E',
                                                          button_cancel_text_color = '#FFFFFF',
                                                          button_cancel_text_color_dark = '#FFFFFF',
                                                          button_cancel_text_color_hover = '#D22C2E',
                                                          button_cancel_text_color_hover_dark = '#D22C2E')