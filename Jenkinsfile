pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-app .'
            }
        }

        stage('Scan Image (Trivy)') {
            steps {
                sh 'trivy image devsecops-app'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm devsecops-app'
            }
        }
    }
}
