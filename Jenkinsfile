pipeline {
    agent any

    environment {
        IMAGE = "webapp:latest"
        CONTAINER = "webapp"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/123-arya/task.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop $CONTAINER || true
                docker rm $CONTAINER || true

                docker run -d \
                  --restart always \
                  -p 5000:5000 \
                  --name $CONTAINER \
                  $IMAGE
                '''
            }
        }
    }
}
