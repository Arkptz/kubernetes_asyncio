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


class V1WebhookConversion(object):
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
        'client_config': 'ApiextensionsV1WebhookClientConfig',
        'conversion_review_versions': 'list[str]'
    }

    attribute_map = {
        'client_config': 'clientConfig',
        'conversion_review_versions': 'conversionReviewVersions'
    }

    def __init__(self, client_config=None, conversion_review_versions=None, local_vars_configuration=None):  # noqa: E501
        """V1WebhookConversion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._client_config = None
        self._conversion_review_versions = None
        self.discriminator = None

        if client_config is not None:
            self.client_config = client_config
        self.conversion_review_versions = conversion_review_versions

    @property
    def client_config(self):
        """Gets the client_config of this V1WebhookConversion.  # noqa: E501


        :return: The client_config of this V1WebhookConversion.  # noqa: E501
        :rtype: ApiextensionsV1WebhookClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """Sets the client_config of this V1WebhookConversion.


        :param client_config: The client_config of this V1WebhookConversion.  # noqa: E501
        :type client_config: ApiextensionsV1WebhookClientConfig
        """

        self._client_config = client_config

    @property
    def conversion_review_versions(self):
        """Gets the conversion_review_versions of this V1WebhookConversion.  # noqa: E501

        conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail.  # noqa: E501

        :return: The conversion_review_versions of this V1WebhookConversion.  # noqa: E501
        :rtype: list[str]
        """
        return self._conversion_review_versions

    @conversion_review_versions.setter
    def conversion_review_versions(self, conversion_review_versions):
        """Sets the conversion_review_versions of this V1WebhookConversion.

        conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail.  # noqa: E501

        :param conversion_review_versions: The conversion_review_versions of this V1WebhookConversion.  # noqa: E501
        :type conversion_review_versions: list[str]
        """
        if self.local_vars_configuration.client_side_validation and conversion_review_versions is None:  # noqa: E501
            raise ValueError("Invalid value for `conversion_review_versions`, must not be `None`")  # noqa: E501

        self._conversion_review_versions = conversion_review_versions

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
        if not isinstance(other, V1WebhookConversion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1WebhookConversion):
            return True

        return self.to_dict() != other.to_dict()
