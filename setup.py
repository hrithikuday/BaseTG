from setuptools import setup, find_packages

setup(
    name="pytgbot",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="XeonModzz",
    description="Minimal Telegram Bot framework using requests"
)
