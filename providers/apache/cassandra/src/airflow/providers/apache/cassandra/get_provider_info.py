# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-apache-cassandra",
        "name": "Apache Cassandra",
        "description": "`Apache Cassandra <https://cassandra.apache.org/>`__.\n",
        "state": "ready",
        "source-date-epoch": 1734527695,
        "versions": [
            "3.7.0",
            "3.6.0",
            "3.5.1",
            "3.5.0",
            "3.4.2",
            "3.4.1",
            "3.4.0",
            "3.3.0",
            "3.2.1",
            "3.2.0",
            "3.1.1",
            "3.1.0",
            "3.0.0",
            "2.1.3",
            "2.1.2",
            "2.1.1",
            "2.1.0",
            "2.0.1",
            "2.0.0",
            "1.0.1",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Apache Cassandra",
                "external-doc-url": "https://cassandra.apache.org/",
                "how-to-guide": ["/docs/apache-airflow-providers-apache-cassandra/operators.rst"],
                "logo": "/docs/integration-logos/cassandra-3.png",
                "tags": ["apache"],
            }
        ],
        "sensors": [
            {
                "integration-name": "Apache Cassandra",
                "python-modules": [
                    "airflow.providers.apache.cassandra.sensors.record",
                    "airflow.providers.apache.cassandra.sensors.table",
                ],
            }
        ],
        "hooks": [
            {
                "integration-name": "Apache Cassandra",
                "python-modules": ["airflow.providers.apache.cassandra.hooks.cassandra"],
            }
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.apache.cassandra.hooks.cassandra.CassandraHook",
                "connection-type": "cassandra",
            }
        ],
        "dependencies": ["apache-airflow>=2.9.0", "cassandra-driver>=3.29.1"],
    }
