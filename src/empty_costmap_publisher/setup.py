from setuptools import setup

package_name = "empty_costmap_publisher"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="ben",
    maintainer_email="chen5713@umn.edu",
    description="Publishes an empty costmap for Nav2.",
    license="MIT License",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "publish = empty_costmap_publisher.publish:main",
        ],
    },
)
