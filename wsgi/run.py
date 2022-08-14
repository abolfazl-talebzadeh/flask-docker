from package import app
import os

# running the docker image in a container DEBUG is an environmental var which sets in
# the command below and it's value refelects in app.run() command 
# docker run -p 5000:5000 -e DEBUG=1 <image-name>
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG')==1)
