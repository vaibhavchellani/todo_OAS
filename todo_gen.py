"""Sample to create Hydra APIDocumentation using doc_writer."""

from doc_writer import HydraDoc, HydraClass, HydraClassProp, HydraClassOp

"""Creating the HydraDoc object, this is the primary class for the Doc"""
API_NAME = "todo"                # Name of the API
BASE_URL = "https://hydrus.com/"    # The base url at which the API is hosted
ENTRY_POINT = "api"                 # The entrypoint where the API will  be accessed
# NOTE: The API will be accessible at BASE_URL + ENTRY_POINT (http://hydrus.com/api/)

api_doc = HydraDoc(API_NAME,
                   "todo list",
                   "simple todo list experiment",
                   ENTRY_POINT,
                   BASE_URL)


"""Creating classes for the API"""
class_title = "task"                      # Title of the Class
class_description = "Class for all the tasks"     # Description of the class
class_uri = "http://hydrus.com/dummyClass"      # URI of class for the HydraClass

task = HydraClass(class_uri,class_title, class_description, endpoint=True)
# NOTE: Setting endpoint=True creates an endpoint for the class itself, this is usually for classes that have single instances.
#       These classes should not ideally have a Collection, although Hydrus will allow creation of Collections for them
#
#

id_uri = "http://schema.org/identifier"
id_title = "Identifier for task"
id_prop = HydraClassProp(id_uri,id_title,required=True, read=True,write=False)

title_uri = "http://schema.org/title"
title_title = "Title for task"
title_prop= HydraClassProp(title_uri, title_title,required=True,read=True,write=False)

dataTime = "http://schema.org/DateTime"
dataTime_title ="Date Time for task"
dataTime_prop = HydraClassProp(dataTime,dataTime_title,required=False,read=True,write=True)


desc_uri = "http://schema.org/identifier"
desc_title="description for task"
desc_prop =HydraClassProp(desc_uri,desc_title,required=True, read=True,write=True)

status_prop=HydraClassProp("http://schema.org/Boolean","Status of task",required=True,read=True,write=True)

addTask = HydraClassOp("Add task",
                       "GET",
                       "vocab:task",
                       None,
                        [{"statusCode": 200, "description": "Task Added"}]
                       )
getTask = HydraClassOp(
                "Get task",
                "POST",
                None,
                "vocab:task",
[{"statusCode": 200, "description": "Task Returned"}]

)

task.add_supported_prop(id_prop)
task.add_supported_prop(title_prop)
task.add_supported_prop(dataTime_prop)
task.add_supported_prop(desc_prop)
task.add_supported_prop(status_prop)
task.add_supported_op(addTask)
task.add_supported_op(getTask)
"""Add the classes to the HydraDoc"""
api_doc.add_supported_class(task, collection=True)
# NOTE: Using collection=True creates a HydraCollection for the class.
#       The name of the Collection is class_.title+"Collection"
#       The collection inherently supports GET and PUT operations

"""Other operations needed for the Doc"""
api_doc.add_baseResource()      # Creates the base Resource Class and adds it to the API Documentation
api_doc.add_baseCollection()    # Creates the base Collection Class and adds it to the API Documentation
api_doc.gen_EntryPoint()        # Generates the EntryPoint object for the Doc using the Classes and Collections


"""Generate the complete API Documentation"""
doc = api_doc.generate()        # Returns the entire API Documentation as a Python dict

if __name__ == "__main__":
    """Print the complete sample Doc in doc_writer_sample_output.py."""
    import json

    dump = json.dumps(doc, indent=4, sort_keys=True)
    doc = '''"""\nGenerated API Documentation sample using doc_writer_sample.py.\n\ndoc = %s\n"""''' % dump
    # Python does not recognise null, true and false in JSON format, convert them to string
    doc = doc.replace('true', '"true"')
    doc = doc.replace('false', '"false"')
    doc = doc.replace('null', '"null"')
    f = open("testDoc_output.py", "w")
    f.write(doc)
    f.close()