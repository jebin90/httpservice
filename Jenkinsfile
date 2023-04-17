pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip3 install pytest'
                sh 'nohup python3 -m pytest &'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t my-http-service .'
            }
        }
        
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'jenkinsaccess', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker tag my-http-service jebin90/my-http-service'
                    sh 'docker push jebin90/my-http-service'
                }
            }
        }
    }
}
