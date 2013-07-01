import face_recognition as fc #import facial recognition functions
import web #import web.py framework


# copies the user specified file to a local file

def copy_file(filedir, person):
    if 'imagefile' in person: # to check if the file-object is created
        filepath=person.imagefile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
        filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
        newFilename = filedir +'\\'+ filename # gets the filename and location of cloned file.
        fout = open(newFilename,'wb') # creates the file where the uploaded file should be stored
        fout.write(person.imagefile.file.read()) # writes the uploaded file to the newly created file.
        fout.close() # closes the file, upload complete.
        return newFilename # copy file location 

        
render = web.template.render('templates/') # uses the html files as templates

urls = ('/', 'faceTrainer',
        '/rec', 'faceRecognizer') #define urls for each class

class faceTrainer:
    def GET(self):
        return render.index(' ') #render training page with no output 

        
    def POST(self): 
        person = web.input(imagefile={}) # read user input
        filedir = 'C:\Documents and Settings\Rigs\Desktop\RESTOpenCV\saved_faces' # directory to store the file in.
        newFilename = copy_file(filedir, person)
  
        name = person['nameface'] # gets the name of the person
        fc.train_with_file(newFilename, name) # calls the training function from face_recognizer module
        
        output = '%s was added to the model' %name
            
        return render.index(output) # renders the page with the output

class faceRecognizer:
    def GET(self):
        result = 'No results yet'
        return render.rec(result) # render recognizing page with no output
        
    def POST(self):
        person = web.input(imagefile={}) # read user input
        filedir = 'C:\Documents and Settings\Rigs\Desktop\RESTOpenCV\other_faces' # directory to store the file in.
        newFilename = copy_file(filedir, person)
            
        result = fc.recognize_face(newFilename) # calls the recognizing function from face_recognizer module
                                                # and stores results  
            
        return render.rec(result) # render the page with the output.
        
        
if __name__ == "__main__":
   app = web.application(urls, globals()) # defines the application
   app.run() # runs the application