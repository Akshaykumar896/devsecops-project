pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-app .'
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                docker run --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                aquasec/trivy image \
                --exit-code 1 \
                --severity CRITICAL \
                devsecops-app
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm devsecops-app'
            }
        }
    }
}
