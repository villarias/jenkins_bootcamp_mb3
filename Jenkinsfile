pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    parameters {
        string(name: 'NOMBREALUMNO', defaultValue: 'PABLO', description: 'Nombre del alumno')
        string(name: 'EDAD', defaultValue: '27', description: 'Edad')
    }

    stages {

        stage('Checkout') {
            steps {
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
                    sh '''
                        . venv/bin/activate
                        python3 src/main.py "$NOMBREALUMNO" "$EDAD"
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
