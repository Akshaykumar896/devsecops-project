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
                sh '''
                docker run --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                aquasec/trivy image --exit-code 1 --severity HIGH,CRITICAL devsecops-app
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
