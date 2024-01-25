import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
        """ Instances of new model """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            
    def __str__(self):
        """" Returns a string representation of the new instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
    
    def save(self):
        """Updates in update column with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """Convert instance to dictionary format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({ '__class__':
            				(str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary