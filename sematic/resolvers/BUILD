sematic_py_lib(
    name = "local_resolver",
    srcs = ["local_resolver.py"],
    deps = [
        ":silent_resolver",
        "//sematic:abstract_future",
        "//sematic:api_client",
        "//sematic:config",
        "//sematic/db/models:artifact",
        "//sematic/db/models:edge",
        "//sematic/db/models:factories",
        "//sematic/db/models:run",
    ],
)

sematic_py_lib(
    name = "state_machine_resolver",
    srcs = ["state_machine_resolver.py"],
    deps = [
        "//sematic:abstract_future",
        "//sematic:resolver",
    ],
)

sematic_py_lib(
    name = "silent_resolver",
    srcs = ["silent_resolver.py"],
    deps = [
        "//sematic:abstract_future",
        "//sematic/resolvers:state_machine_resolver",
    ],
)

sematic_py_lib(
    name = "cloud_resolver",
    srcs = ["cloud_resolver.py"],
    deps = [
        ":local_resolver",
        "//sematic:abstract_future",
        "//sematic/db/models:artifact",
        "//sematic/db/models:edge",
        "//sematic/db/models:run",
        requirement("kubernetes"),
        requirement("cloudpickle"),
    ],
)

sematic_py_lib(
    name = "resource_requirements",
    srcs = ["resource_requirements.py"],
    deps = [],
)

sematic_py_lib(
    name = "worker",
    srcs = ["worker.py"],
    deps = [
        "//sematic:abstract_future",
        "//sematic:api_client",
        "//sematic:future",
        "//sematic/db/models:artifact",
        "//sematic/db/models:edge",
        "//sematic/db/models:factories",
        "//sematic/resolvers:cloud_resolver",
        requirement("cloudpickle"),
    ],
)

exports_files([
    "worker.py",
])
