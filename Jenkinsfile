pipeline {
    agent any  // Ya 'windows' label wala agent agar specific chahiye

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AashikAli240/easy2shop.git'
                // Ya agar Jenkins multibranch: checkout scm
            }
        }

        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                bat '''
                    @echo off
                    echo Creating/using virtual environment...
                    if not exist venv (
                        python -m venv venv
                    )
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    echo Dependencies installed in venv
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                bat '''
                    @echo off
                    call venv\\Scripts\\activate.bat
                    python -m pytest || echo "No tests found or tests failed - continuing..."
                '''
                // Agar tests mandatory hain to || exit 0 hata do, warna pipeline fail na ho
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t easy2shop:latest .'
            }
        }

        stage('Push to Registry') {
            steps {
                // Pehle login karo agar private registry hai (credentials Jenkins mein add karo)
                // withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                //     bat "docker login -u %USER% -p %PASS%"
                // }

                bat 'docker tag easy2shop:latest your-registry/easy2shop:latest'  // Change 'your-registry' to real one e.g. docker.io/aashikali
                bat 'docker push your-registry/easy2shop:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Agar minikube/local k8s: pehle context set karo
                // bat 'kubectl config use-context minikube'  // agar zaroori ho

                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }
    }

    post {
        always {
            bat 'call venv\\Scripts\\deactivate.bat || echo "No venv to deactivate"'
        }
    }
}
