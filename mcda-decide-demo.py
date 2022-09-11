import PySimpleGUI as sg
import subprocess
from textwrap import wrap

#def main_win():
    #return sg.Window("MCDA Exploration",tab_group, resizable=True, location=(400,300), finalize=True)

def open_window(question, explanation):
    layout = [[sg.Text("Question: ", background_color='Grey')],[sg.Text(question)],
              [sg.Multiline(explanation, size=(30, 15), key='-TEXT2-', autoscroll=True)]]
    window = sg.Window("Explore data", layout, modal=True, resizable = True, background_color='Grey')
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break      
    window.close()
    
def popup(title, filename, message, width=70):

    lines = list(map(lambda line:wrap(line, width=width), message.split('\n')))
    height = sum(map(len, lines))
    message = '\n'.join(map('\n'.join, lines))

    layout = [
        [sg.Image(filename=filename, expand_x=True)],
        [sg.Text(message, size=(width, height), justification='right', expand_x=True)]
    ]
    sg.Window(title, layout, keep_on_top=True, modal=True).read(close=2000)

browse_layout = [
    [sg.Text("Browse folder to open spreadsheet data.", text_color="Black", background_color="White")],
    [sg.Text('Data folder (or leave empty'), sg.InputText()],
    [sg.Button('Browse', key='-BROWSE-'), sg.Button('Cancel')]
]

best_alt_q='What is the best alternative?'
best_alt_ans='There is strong evidence that Amsterdam is the best alternative.\n\nGiven the range of combinations of inputs you have provided, Amsterdam is the most attractive option in 48% of all preference combinations consistent with your inputs. Indeed, it is in the top three options for 99% of combinations of input values.'
best_alt_layout = [[sg.Multiline(best_alt_ans, size=(80,5), key='-TEXT2-', autoscroll=True)]]

exploration_layout01 = [
          [sg.Text("Can you show me the rankings in tabular form?", key='rankings'), sg.Button('Show', key='Show01')],
    ]

exploration_layout02 = [
          [sg.Text("Can you show me the graph of the rankings?", key='graph'), sg.Button('Show', key='Show02')],
    ]

exploration_layout5 = [
          [sg.Text("Can you show me the weights?", key='weights'), sg.Button('Show', key='Show5')],
    ]

exploration_layout6 = [
          [sg.Text("Can you show me the graph of the weights?", key='graph2'), sg.Button('Show', key='Show6')],
    ]
exploration_layout1 = [
          [sg.Text("What is the best alternative?", key='best'), sg.Button('Show', key='Show1')],
          #[sg.Multiline(key='-TEXT1-')] 
    ]

close_cont_q='Any close contenders?'
close_cont_ans='London is a possible contender for optimal location, worthy of further consideration. \nIt is the most attractive alternative in 36% of all preference combinations consistent with your inputs. It also appears to be a good number two choice (38%) as well as a reasonable number three choice (26%).'
close_cont_layout = [[sg.Multiline(close_cont_ans, size=(80,5), key='-TEXT3-', autoscroll=True)]]

exploration_layout2 = [
          [sg.Text('')],
          [sg.Text(close_cont_q, key='close-cont'), sg.Button('Show', key='Show2')],
          #[sg.Multiline(key='-TEXT1-')] 
    ]

other_cont_q='Any other contenders?'
other_cont_ans='Paris is another contender for optimal location. \nGiven the range of combinations of inputs you have provided, Paris ranks first in 15% of all preference combinations. It also appears to be a reasonable number two choice (26%) as well as a good number three choice (56%).'
other_cont_layout = [[sg.Multiline(other_cont_ans, size=(80,5), key='-TEXT3-')]]

exploration_layout3 = [
          [sg.Text('')],
          [sg.Text(other_cont_q, key='other-cont'), sg.Button('Show', key='Show3')],
          #[sg.Multiline(key='-TEXT1-')] 
    ]

inf_alt_q='Any inferior alternatives?'
inf_alt_ans='Warsaw is unlikely to be a good candidate as it does not feature in the top three ranks for any of your preference combinations. Indeed, it ranks last for all preference combinations.'
inf_alt_layout = [[sg.Multiline(inf_alt_ans, size=(80,5), key='-TEXT4-')]]

exploration_layout4 = [
          [sg.Text('')],
          [sg.Text(inf_alt_q, key='inf_alt'), sg.Button('Show', key='Show4')],
          #[sg.Multiline(key='-TEXT1-')] 
    ]


contact_information_array = [
    ['Amsterdam','48.4','35.7','14.7','1.2','0','0','0'],
    ['Berlin','0', '0','0','0','16.7','83.3','0'],
    ['Brussels','0','0','0','18','65.3','16.7','0'],
    ['London','36.1','37.7','25.9','0.3', '0', '0', '0'],
    ['Milan','0.5','0.7','3.7','77.1','18','0','0'],
    ['Paris','15','25.9', '55.7', '3.4', '0','0','0'],
    ['Warsaw','0','0','0','0','0','0','100']
    ]
headings1 = ['Alternative','1','2','3','4','5','6','7']


table_layout = [
            [sg.Text('\t\tFrequency in rank (position)', background_color='White', text_color='Black')],
            [sg.Table(values=contact_information_array, headings=headings1, max_col_width=500,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='left',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=20,
                    tooltip='Rankings Table',
                    expand_x=True)]
]

tab_group = [
                [sg.TabGroup(
                    [[sg.Tab('Browse', browse_layout, title_color='Red', background_color='White',
                            tooltip='Instructions', element_justification= 'left'),
                    sg.Tab('Explore Ranking', exploration_layout01,title_color='Black',background_color='White'),
                    sg.Tab('Explain Ranking', exploration_layout1, title_color='Blue',background_color='White'),
                    sg.Tab('Explore Weights', exploration_layout5, title_color='Blue',background_color='White'),      
                    sg.Tab('Explain Weights', exploration_layout6, title_color='Blue',background_color='White'),
                      ]], 
                    
                    tab_location='centerleft',
                    title_color='Black', tab_background_color='White',selected_title_color='White',
                    selected_background_color='Grey', border_width=5, key='-TABS-', expand_x=True, expand_y=True), sg.Button('Exit')
                ]                      
            ]

col1 = sg.Column(tab_group, scrollable=True, size=(600,500), vertical_scroll_only=True)
tab_group_scrollable_layout = [[col1]]
#Define Window
window=sg.Window("MCDA Exploration", tab_group_scrollable_layout,
                 auto_size_text=True,
                auto_size_buttons=True, resizable=True, grab_anywhere=False, border_depth=5,
                default_element_size=(45,1), finalize=True)

col1.expand(True, True)
#window.TKroot.minsize(400,500)

def main():
    #window1, window2 = main_win(), None        # start off with 1 window open
    while True:
        event,values=window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-BROWSE-":
            try:
                subprocess.Popen(r'explorer /select, "C:\Users\gcdem\Dropbox\George-Nadia papers\MAVT Explanations Theo\"')
            except Exception as e:
                print("Error: ", e)
        if event == 'Show01':
            window.extend_layout(window['Explore Ranking'], table_layout)
            window.extend_layout(window['Explore Ranking'], exploration_layout02)
        if event == 'Show02':
            popup('Rankings', 'C:/tmp/image001.png', '')
        if event == 'Show1':
        #window['-TEXT1-'].update(explanation)
        #open_window(question, explanation)
        #contact_information_array.append([values['-NAME-'], values['-ADDRESS-'], values['-PHONE_NUMBER-']])
        #window['-TABLE-'].update(values=contact_information_array)
            window.extend_layout(window['Explain Ranking'], best_alt_layout)
            window.extend_layout(window['Explain Ranking'], exploration_layout2)
        if event == 'Show2':
            window.extend_layout(window['Explain Ranking'], close_cont_layout)
            window.extend_layout(window['Explain Ranking'], exploration_layout3)
        if event == 'Show3':
            window.extend_layout(window['Explain Ranking'], other_cont_layout)
            window.extend_layout(window['Explain Ranking'], exploration_layout4)
        if event == 'Show4':
            window.extend_layout(window['Explain Ranking'], inf_alt_layout)
 
    window.close()

if __name__ == '__main__':
    main()