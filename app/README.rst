  cmak2zk:
    image: ghcr.io/eshepelyuk/dckr/cmak2zk:latest
    restart: on-failure
    command:
      - 'zoo:2181'
      - '/app/etc/clusters.yaml'
    depends_on:
      - "zoo" 
    volumes:
      - "${PWD}/clusters.yaml:/app/etc/clusters.yaml:ro"

kafka:
    image: wurstmeister/kafka 
    ports:
      - "9092:9092"
    container_name: kafka
    environment:
      - KAFKA_ADVERTISED_HOST_NAME=192.168.99.100
      - KAFKA_CREATE_TOPICS=shipp
      - KAFKA_ZOOKEEPER_CONNECT=zoo:2181
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./logs:/logs









        zoo1:
    image: confluentinc/cp-zookeeper:7.1.1
    hostname: zoo1
    container_name: zoo1
    ports:
      - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_SERVER_ID: 1
      ZOOKEEPER_SERVERS: zoo1:2888:3888


  kafka1:
    image: confluentinc/cp-kafka:7.1.1
    hostname: kafka1
    container_name: kafka1
    ports:
      - "9092:9092"
      - "9999:9999"
    environment:
      KAFKA_ADVERTISED_LISTENERS: LISTENER_DOCKER_INTERNAL://kafka1:19092,LISTENER_DOCKER_EXTERNAL://${DOCKER_HOST_IP:-127.0.0.1}:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: LISTENER_DOCKER_INTERNAL:PLAINTEXT,LISTENER_DOCKER_EXTERNAL:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: LISTENER_DOCKER_INTERNAL
      KAFKA_ZOOKEEPER_CONNECT: "zoo1:2181"
      KAFKA_BROKER_ID: 1
      KAFKA_LOG4J_LOGGERS: "kafka.controller=INFO,kafka.producer.async.DefaultEventHandler=INFO,state.change.logger=INFO"
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_JMX_PORT: 9999
      KAFKA_JMX_HOSTNAME: ${DOCKER_HOST_IP:-127.0.0.1}
      KAFKA_AUTHORIZER_CLASS_NAME: kafka.security.authorizer.AclAuthorizer
      KAFKA_ALLOW_EVERYONE_IF_NO_ACL_FOUND: "true"
    depends_on:
      - zoo1


  kafka_manager:
    image: hlebalbau/kafka-manager:stable
    container_name: kafka-manager
    restart: always 
    ports: 
     - 9000:9000
    environment:
      - ZK_HOSTS=zoo1:2181
      - JMX_PORT=9999