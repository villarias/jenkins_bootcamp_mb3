pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }
    parameters {
        string(name: 'NOMBREALUMNO', defaultValue: 'PABLO', description: 'NOMBREALUMNO')
        string(name: 'EDAD', defaultValue: '27', description: 'EDAD')
        file(name: 'INPUT_FILE')
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
                sh '''#!/bin/bash
        source venv/bin/activate
        python3 main.py "$NOMBREALUMNO" "$EDAD" "$INPUT_FILE"
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
