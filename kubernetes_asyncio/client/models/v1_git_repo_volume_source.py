# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.22.6
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1GitRepoVolumeSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'directory': 'str',
        'repository': 'str',
        'revision': 'str'
    }

    attribute_map = {
        'directory': 'directory',
        'repository': 'repository',
        'revision': 'revision'
    }

    def __init__(self, directory=None, repository=None, revision=None, local_vars_configuration=None):  # noqa: E501
        """V1GitRepoVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._directory = None
        self._repository = None
        self._revision = None
        self.discriminator = None

        if directory is not None:
            self.directory = directory
        self.repository = repository
        if revision is not None:
            self.revision = revision

    @property
    def directory(self):
        """Gets the directory of this V1GitRepoVolumeSource.  # noqa: E501

        Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.  # noqa: E501

        :return: The directory of this V1GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this V1GitRepoVolumeSource.

        Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.  # noqa: E501

        :param directory: The directory of this V1GitRepoVolumeSource.  # noqa: E501
        :type directory: str
        """

        self._directory = directory

    @property
    def repository(self):
        """Gets the repository of this V1GitRepoVolumeSource.  # noqa: E501

        Repository URL  # noqa: E501

        :return: The repository of this V1GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this V1GitRepoVolumeSource.

        Repository URL  # noqa: E501

        :param repository: The repository of this V1GitRepoVolumeSource.  # noqa: E501
        :type repository: str
        """
        if self.local_vars_configuration.client_side_validation and repository is None:  # noqa: E501
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501

        self._repository = repository

    @property
    def revision(self):
        """Gets the revision of this V1GitRepoVolumeSource.  # noqa: E501

        Commit hash for the specified revision.  # noqa: E501

        :return: The revision of this V1GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V1GitRepoVolumeSource.

        Commit hash for the specified revision.  # noqa: E501

        :param revision: The revision of this V1GitRepoVolumeSource.  # noqa: E501
        :type revision: str
        """

        self._revision = revision

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1GitRepoVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1GitRepoVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
