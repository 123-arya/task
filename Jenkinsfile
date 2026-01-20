pipeline {
    agent any

    environment {
        IMAGE_NAME = "arya08/webapp"
        IMAGE_TAG  = "web"
    }
    stages{
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t web .'
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'arya08',
                    passwordVariable: 'AaZz@@1234'
                )]) { 
                    sh 'echo "AaZz@@1234" | docker login -u "arya08" --password-stdin'
               }
            }
        }
         stage('Push Image') {
            steps {
                sh 'docker push arya08/webapp:web'
            }
        }
    }
}
