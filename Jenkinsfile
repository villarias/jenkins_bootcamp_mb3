pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        PYTHON = 'python3'
    }

    parameters {
        string(name: 'NOMBREALUMNO', defaultValue: 'PABLO')
        string(name: 'EDAD', defaultValue: '27')
        file(name: 'INPUT_FILE')
    }

    stages {

        stage('Checkout') {
            steps {
                dir('src') {
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    $PYTHON -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f src/requirements.txt ]; then
                        pip install -r src/requirements.txt
                    fi
                '''
            }
        }

        stage('Run Script') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''#!/bin/bash
                    source venv/bin/activate

                    echo "Copiando archivo desde @tmp..."
                    cp "$WORKSPACE@tmp/$INPUT_FILE" .

                    echo "Archivo disponible en workspace:"
                    ls -l "$INPUT_FILE"

                    $PYTHON src/main.py "$NOMBREALUMNO" "$EDAD" "$INPUT_FILE"
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado (always)'
        }
        failure {
            echo 'El pipeline falló'
        }
        success {
            echo 'Pipeline exitoso'
        }
    }
}
