from office365.sharepoint.entity import Entity


class SPMachineLearningPublication(Entity):
    @property
    def entity_type_name(self):
        return "Microsoft.Office.Server.ContentCenter.SPMachineLearningPublication"
