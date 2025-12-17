pipeline {
    agent any

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
                    sh '''
                    source venv/bin/activate

                    echo "Archivo subido: $INPUT_FILE"

                    cp "$INPUT_FILE" input.txt
                    ls -l input.txt

                    python3 src/main.py "$NOMBREALUMNO" "$EDAD" "input.txt"
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
