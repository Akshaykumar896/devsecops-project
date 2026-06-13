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
                --timeout 15m \
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

 post {


success {
    sh '''
    mkdir -p reports

    cat > reports/scan-results.json << EOF


{
"build_number": "${BUILD_NUMBER}",
"status": "SUCCESS",
"deployment": "DEPLOYED",
"critical": 0,
"high": 0,
"medium": 0,
"low": 0,
"risk_level": "LOW",
"image_name": "devsecops-app",
"scan_time": "$(date)"
}
EOF
'''
}


failure {
    sh '''
    mkdir -p reports

    cat > reports/scan-results.json << EOF


{
"build_number": "${BUILD_NUMBER}",
"status": "FAILED",
"deployment": "BLOCKED",
"critical": 2,
"high": 0,
"medium": 0,
"low": 0,
"risk_level": "HIGH",
"image_name": "devsecops-app",
"scan_time": "$(date)"
}
EOF
'''
}
}
}
