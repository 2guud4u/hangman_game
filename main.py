from flask import Flask, render_template, request  
import code


app = Flask(__name__)

# the number of letters
num_letter = 0
# letters used
used_letter = []
# current progress of guessing
current = ''
old_current=''
# computer guess
next_let = ''
buttons_pressed = False
health = 6
image="Hangman1.png"

@app.route('/')
def home():
    global health
    health=6
    return render_template("index.html")
    

# finding the number of letters in word
# TODO get computer first guess
@app.route('/length', methods=['POST', 'GET'])
def dropdown():
    global image
    # letters used
    global used_letter 
    # number of letters in 
    global num_letter
    global current
    global health
    global next_let
    global old_current
    global new_current
    
    if request.method=="POST":
      used_letter = []
      num_letter = int(request.form.get("answer"))
      # ADD THE COMPUTER GENERATED NEXT LETTER
      current = "." * num_letter
      print(current)
      print(used_letter)
      old_current=""
      new_current=""
      next_let = code.newlist(current, used_letter)
      used_letter.append(next_let)
      return render_template("hangman.html", guessed = used_letter, next_letter = next_let, data = num_letter, progress = current, healthy=health)

 
 
# submit hangman.html
@app.route('/word', methods=['POST', 'GET'])
def word_update():
    global num_letter
    global used_letter
    global next_let
    global health
    global current
    global image
    global old_current
    global buttons_pressed
    if request.method=="POST":
      # current = ""
      print("HERE IS CURRENT TO START "+ current)
      print("num letter is " + str(num_letter))
      for num in range(0, num_letter):
        value = request.form.get((str(num)+"/"))
        print("here is the value "+ str(value))
        if value == None and current[num]=='.':
          current = current[0:num] + "." + current[num+1:]
          
        elif not current[num].isalpha():
          print("\n\nINPUTTED THE LETTER" + current + "\n\n")
          current = current[0:num]  + next_let + current[num+1:]
      print("here is current " + current + " and used letter "+ str(used_letter))
      buttons_pressed=False
      new_current=""
      for i in current:
          if i != '.':
              new_current+=i
      for i in range(0, len(new_current)):
            if len(new_current) is not len(old_current):
                old_current = new_current
                buttons_pressed=True
                break
            if new_current[i] is not old_current[i]:
                print("New Current "+new_current[i])
                print("Old Current "+old_current[i])
                old_current=new_current
                buttons_pressed=True
                break
      if buttons_pressed:
          buttons_pressed=False
      else:
          health-=1
          buttons_pressed=False     
      if health==6:
          image="Hangman1.png"
      if health==5:
          image="Hangman2.png"
      if health==4:
          image="Hangman3.png"
      if health==3:
          image="Hangman4.png"
      if health==2:
          image="Hangman5.png"
      if health==1:
          image="Hangman6.png"
      if health==0:
          image="Hangman7.png"
          health=6
          return render_template("gameover.html")

            
      if '.' not in current:
          health=6
          return render_template("win.html")
      # GET THE NEXT LETTER HERE!!!!!
      next_let = code.newlist(current, used_letter)
      # ADD TO USED LETTERS LIST
      used_letter.append(next_let)

      
      
      return render_template("hangman.html", guessed = used_letter, next_letter = next_let, progress = current, data = num_letter, healthy=health)
 


if __name__=="__main__":
    app.run(debug=False, host="0.0.0.0")


