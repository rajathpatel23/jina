ac_table = {
    'commands': [
        '--help',
        '--version',
        '--version-full',
        'hello',
        'executor',
        'flow',
        'ping',
        'gateway',
        'hub',
        'help',
        'pea',
        'pod',
        'client',
        'export-api',
    ],
    'completions': {
        'hello fashion': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--index-labels-url',
            '--query-data-url',
            '--query-labels-url',
            '--num-query',
            '--top-k',
        ],
        'hello chatbot': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port-expose',
            '--parallel',
            '--unblock-query-flow',
        ],
        'hello multimodal': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port-expose',
            '--unblock-query-flow',
        ],
        'hello fork': ['--help', 'fashion', 'chatbot', 'multimodal'],
        'hello': ['--help', 'fashion', 'chatbot', 'multimodal', 'fork'],
        'executor': [
            '--help',
            '--name',
            '--workspace',
            '--k8s-namespace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--static-routing-table',
            '--routing-table',
            '--zmq-identity',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--hosts-in-connect',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--native',
            '--num-part',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--grpc-data-requests',
            '--runs-in-docker',
            '--dump-path',
            '--k8s-connection-pool',
            '--k8s-no-connection-pool',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
            '--install-requirements',
            '--force',
        ],
        'flow': [
            '--help',
            '--name',
            '--workspace',
            '--k8s-namespace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--static-routing-table',
            '--routing-table',
            '--uses',
            '--env',
            '--inspect',
            '--infrastructure',
        ],
        'ping': ['--help', '--timeout', '--retries', '--print-response'],
        'gateway': [
            '--help',
            '--name',
            '--workspace',
            '--k8s-namespace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--static-routing-table',
            '--routing-table',
            '--zmq-identity',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--hosts-in-connect',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--native',
            '--num-part',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--grpc-data-requests',
            '--runs-in-docker',
            '--dump-path',
            '--k8s-connection-pool',
            '--k8s-no-connection-pool',
            '--prefetch',
            '--title',
            '--description',
            '--cors',
            '--default-swagger-ui',
            '--no-debug-endpoints',
            '--no-crud-endpoints',
            '--expose-endpoints',
            '--uvicorn-kwargs',
            '--compress',
            '--compress-min-bytes',
            '--compress-min-ratio',
            '--protocol',
            '--host',
            '--proxy',
            '--port-expose',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
            '--k8s-uses-init',
            '--k8s-mount-path',
            '--k8s-init-container-command',
            '--k8s-custom-resource-dir',
            '--dynamic-routing',
        ],
        'hub new': [
            '--help',
            '--name',
            '--path',
            '--advance-configuration',
            '--description',
            '--keywords',
            '--url',
            '--add-dockerfile',
        ],
        'hub push': [
            '--help',
            '--no-usage',
            '--dockerfile',
            '--tag',
            '--force',
            '--secret',
            '--public',
            '--private',
        ],
        'hub pull': ['--help', '--no-usage', '--install-requirements', '--force'],
        'hub': ['--help', 'new', 'push', 'pull'],
        'help': ['--help'],
        'pea': [
            '--help',
            '--name',
            '--workspace',
            '--k8s-namespace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--static-routing-table',
            '--routing-table',
            '--zmq-identity',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--hosts-in-connect',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--native',
            '--num-part',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--grpc-data-requests',
            '--runs-in-docker',
            '--dump-path',
            '--k8s-connection-pool',
            '--k8s-no-connection-pool',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
            '--install-requirements',
            '--force',
        ],
        'pod': [
            '--help',
            '--name',
            '--workspace',
            '--k8s-namespace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--static-routing-table',
            '--routing-table',
            '--zmq-identity',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--hosts-in-connect',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--native',
            '--num-part',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--grpc-data-requests',
            '--runs-in-docker',
            '--dump-path',
            '--k8s-connection-pool',
            '--k8s-no-connection-pool',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
            '--install-requirements',
            '--force',
            '--uses-before',
            '--uses-after',
            '--parallel',
            '--shards',
            '--replicas',
            '--polling',
            '--scheduling',
            '--external',
            '--peas-hosts',
            '--pod-role',
            '--no-dynamic-routing',
            '--connect-to-predecessor',
            '--k8s-uses-init',
            '--k8s-mount-path',
            '--k8s-init-container-command',
            '--k8s-custom-resource-dir',
        ],
        'client': [
            '--help',
            '--host',
            '--proxy',
            '--port',
            '--https',
            '--asyncio',
            '--protocol',
            '--prefetch',
        ],
        'export-api': ['--help', '--yaml-path', '--json-path', '--schema-path'],
    },
}
