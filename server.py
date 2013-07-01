import face_recognition as fc
import web

render = web.template.render('templates/')

urls = ('/', 'faceTrainer',
        '/rec', 'faceRecognizer')

class faceTrainer:
    def GET(self):
        # web.header("Content-Type","text/html; charset=utf-8")
        return render.index(' ')

    def POST(self):
        person = web.input(trainfile={})
        filedir = 'C:\Documents and Settings\Rigs\Desktop\RESTOpenCV\saved_faces' # change this to the directory you want to store the file in.
        if 'trainfile' in person: # to check if the file-object is created
            filepath=person.trainfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            newFilename = filedir +'\\'+ filename # gets the filename and location of cloned file.
            print newFilename
            fout = open(newFilename,'wb') # creates the file where the uploaded file should be stored
            fout.write(person.trainfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
            
            
            name = person['nameface'] # gets the name of the person
            fc.train_with_file(newFilename, name)
            output = '%s was added to the model' %name
        return render.index(output)

class faceRecognizer:
    def GET(self):
        result = 'No results yet'
        return render.rec(result)
        
    def POST(self):
        person = web.input(recognizefile={})
        filedir = 'C:\Documents and Settings\Rigs\Desktop\RESTOpenCV\other_faces' # change this to the directory you want to store the file in.
        if 'recognizefile' in person: # to check if the file-object is created
            filepath=person.recognizefile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            newFilename = filedir +'\\'+ filename # gets the filename and location of cloned file.
            print newFilename
            fout = open(newFilename,'wb') # creates the file where the uploaded file should be stored
            fout.write(person.recognizefile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
            
            result = fc.recognize_face(newFilename)
            # print render(result)
            
        return render.rec(result)
        
        
if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()