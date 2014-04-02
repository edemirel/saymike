from flask import Flask, render_template, request
import datetime,cgi,os,cgitb,sys,time
 
app = Flask(__name__)
cgitb.enable()
sys.path.insert(0,"/usr/bin/espeak")
       
def play(something):
        os.system('mpg321 -q ~/../home/pi/mike_sb/"{0}".mp3'.format(something))
        #time.sleep(5)
        #os.system('sudo killall mpg321')
       
@app.route("/saymike", methods=['GET','POST'])
def speakmike():
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        templateData = {
                'title' : 'Ege Demirel',
                'time'  : timeString,
                'choice': 'BigSigh'}
               
        if request.method == 'GET':    
                return render_template('saymike.html', **templateData)
               
        else:
                test=request.values['chat']
                templateData['choice'] = test
               
                #print type(test)
        #play(test)
                return render_template('saymike.html', **templateData)
 
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug=True)