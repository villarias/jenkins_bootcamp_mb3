pipeline {
    agent any

    options {
        // Evita que Jenkins haga checkout automático y borre el archivo subido
        skipDefaultCheckout(true)
    }

    environment {
        PYTHON = 'python3'
    }

    parameters {
        string(
            name: 'NOMBREALUMNO',
            defaultValue: 'PABLO',
            description: 'Nombre del alumno'
        )
        string(
            name: 'EDAD',
            defaultValue: '27',
            description: 'Edad'
        )
        file(
            name: 'INPUT_FILE',
            description: 'Archivo a leer por el script Python'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                // Checkout en subdirectorio para no borrar INPUT_FILE
                dir('src') {
                    checkout scm
                }
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

                    echo "Archivo recibido: $INPUT_FILE"
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
        success {
            echo 'Pipeline ejecutado correctamente'
        }
        failure {
            echo 'El pipeline falló'
        }
    }
}
