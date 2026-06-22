# cicd-jenkins-ansible-docker
# Pipeline CI/CD Automatizado con Jenkins, Ansible y Docker

Este proyecto implementa un flujo completo de Integración y Despliegue Continuo (CI/CD) para una aplicación web. Automatiza desde la gestión del código fuente y la ejecución de pruebas unitarias hasta el aprovisionamiento de la infraestructura y el despliegue en entornos aislados de contenedores.

## 🚀 Arquitectura y Flujo del Pipeline

El ciclo de vida del desarrollo sigue el siguiente flujo automatizado:

1. **Control de Versiones (GitLab):** El desarrollo se gestiona mediante Git. Al realizar un `push` en la rama configurada, se dispara un webhook hacia el servidor de automatización.
2. **Orquestación (Jenkins):** Jenkins detecta el cambio y arranca el pipeline definido en el `Jenkinsfile`.
3. **Fase de Testing (JUnit):** Se ejecutan los tests automatizados sobre la aplicación web, generando reportes en formato JUnit XML para validar la estabilidad del código.
4. **Fase de Aprovisionamiento (Ansible):** Si los tests pasan con éxito, Ansible gestiona la configuración de los entornos, asegurando la idempotencia del sistema.
5. **Despliegue y Aislamiento (Docker):** La aplicación se empaqueta y se despliega utilizando Docker y Docker-Compose, levantando los servicios necesarios en contenedores independientes (ej. Pre-producción y Cliente).

![Arquitectura y Flujo del Pipeline](Pipeline-Architecture.jpg)

## 🛠️ Tecnologías Utilizadas

* **CI/CD:** Jenkins (Pipelines declarativos)
* **Gestión de Configuración / IaC:** Ansible
* **Contenedores:** Docker & Docker-Compose
* **Sistemas de Control de Versiones:** GitLab
* **Testing Framework:** JUnit
* **Entorno de Servidores:** Linux (Ubuntu/Debian)

## 📁 Estructura del Proyecto

* `/aprovisionamiento`: Contiene los playbooks de Ansible y los archivos de configuración de Docker para el despliegue automatizado.
* `/web`: Código fuente de la aplicación y la suite de pruebas unitarias.

## 🔧 Requisitos Previos

Para replicar este entorno localmente, necesitas tener instalado:
* Docker & Docker-Compose
* Ansible (versión X.X o superior)
* Acceso a una instancia de Jenkins con los plugins necesarios instalados (Git, JUnit, Ansible).

## 🚀 Cómo Ejecutar el Proyecto (Modo Local)

Si deseas probar el despliegue manual o la configuración de los contenedores sin el pipeline de Jenkins, sigue estos pasos:

1. **Clonar el repositorio:**
```bash
   git clone [https://github.com/TU_USUARIO/cicd-jenkins-ansible-docker.git](https://github.com/TU_USUARIO/cicd-jenkins-ansible-docker.git)
   cd cicd-jenkins-ansible-docker
