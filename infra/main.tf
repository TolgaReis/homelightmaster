resource "docker_network" "iot_network" {
    name = "iot_network"
}

resource "docker_container" "mongodb" {
    name         = "mongodb"
    image        = "mongo"
    network_mode = docker_network.iot_network.name
}

resource "docker_container" "mosquitto" {
    name         = "mosquitto"
    image        = "eclipse-mosquitto"
    ports {
        internal = 1883
        external = 1883
    }
    network_mode = docker_network.iot_network.name
}
