pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                bat 'start /B python -m pytest'
            }
        }
        
        stage('Build') {
            steps {
                bat 'docker build -t my-http-service .'
            }
        }
        
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'jenkinsaccess', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat 'docker login'
                    bat 'docker tag my-http-service jebin90/my-http-service'
                    bat 'docker push jebin90/my-http-service'
                }
            }
        }
    }
}
