    import pkgutil
    import pkg_resources

    package_name = 'Pillow'
    if pkgutil.find_loader(package_name):
        print(f'Пакет {package_name} установлен.')
        distribution = pkg_resources.get_distribution(package_name)
        package_version = distribution.version
        print(f'Версия пакета {package_name} - {package_version}')
    else:
        print(f'Пакет {package_name} не установлен.')
