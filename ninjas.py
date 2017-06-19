from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninja', methods =['POST'])
def ninja():
    return render_template('ninja.html',text=text, image=image)

    # text = 'TMNT'
    # image = tmnt.png

# @ app.route('/ninja/<color>')
#     def ninjacolor(color):
#         if color == 'blue'
#             text = 'Leonardo'
#         elif color == 'red'
#             text = 'Raphael'
#         elif color == 'orange'
#             text = 'Michelangelo'
#         elif color == 'purple'
#             text = 'Donatello'
#         else:
#             text = '404_not_found'
            #rename april jpeg to 404_no_found

        image = text.lower()+'.jpeg''

        return renfer_template('ninja.html', text=text, image=image')









@app.route('/ninja/blue', methods =['POST'])
def blue():
    return render_template('leonardo.html')

@app.route('/ninja/orange', methods =['POST'])
def orange():
    return render_template('michel.html')

@app.route('/ninja/red', methods =['POST'])
def red():
    return render_template('raphael.html')

@app.route('/ninja/purple', methods =['POST'])
def purple():
    return render_template('donatello.html')


app.run(debug=True)