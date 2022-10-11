from dependency_network_metamodel.models.objects.cvss import CVSS

class CVE:
    
    def __init__(
        self,
        id: str,
        source: str,
        description: str,
        cpes: list[str],
        cvss: 'CVSS'
    ) -> None:

        self.id  = id
        self.source = source
        self.description = description
        self.cpes = cpes
        self.cvss = cvss
