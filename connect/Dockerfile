# Kafka Connect image with JDBC Sink and Postgres driver
FROM confluentinc/cp-kafka-connect:7.6.0

# Install JDBC Sink connector via Confluent Hub
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.4

# Install curl to fetch the Postgres JDBC driver
USER root
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Add Postgres JDBC driver
RUN curl -fsSL -o /usr/share/confluent-hub-components/confluentinc-kafka-connect-jdbc/lib/postgresql-42.7.4.jar \
    https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.4/postgresql-42.7.4.jar

USER appuser
