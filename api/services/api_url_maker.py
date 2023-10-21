from typing import Optional


class MakeAPIUrlFromPackage:
    def __call__(self, package, additional: Optional[str] = None):
        url: str = '/'.join(str(package.__package__).split('.'))
        if additional:
            url = '/'.join([url, additional])
        return url.replace('//', '/').replace('\\', '/')
