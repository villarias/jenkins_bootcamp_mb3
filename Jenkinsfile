pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh '''
                    $PYTHON --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    $PYTHON -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                    . venv/bin/activate
                    $PYTHON main.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado'
        }
        failure {
            echo 'El pipeline falló'
        }
    }
}
