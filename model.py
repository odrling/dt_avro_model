from pathlib import Path

from tempfile import NamedTemporaryFile
from pyecore.resources import ResourceSet, URI

rset = ResourceSet()
path = Path(__file__).parent / "BPMN20.ecore"
resource = rset.get_resource(URI(str(path)))

for mm_root in resource.contents:
    rset.metamodel_registry[mm_root.nsURI.replace("-XMI", "")] = mm_root.getEClassifier('DocumentRoot')
    print(mm_root)
    print(mm_root.nsURI)


class Model:

    def __init__(self):
        self.model = None

    def load_xmi(self, xmi_data: str):

        with NamedTemporaryFile('w') as f:
            f.write(xmi_data)
            f.flush()
            resource = rset.get_resource(URI(f.name))

            model_root = resource.contents[0]
            self.model = model_root
