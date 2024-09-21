"""Configuration module for managing application settings."""

from typing import List, Dict, Any, Type, Tuple

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    TomlConfigSettingsSource,
    JsonConfigSettingsSource,
    YamlConfigSettingsSource,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    """Settings class for managing application configuration.

    This class extends Pydantic's BaseSettings to load and manage configuration
    options for the application, allowing customization from various sources.
    """

    remote_targets: List[Dict[str, Any]] = []

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="eolic_", extra="allow"
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        """Customize the sources of configuration settings for the application.

        This method allows the addition of custom configuration sources, such as
        JSON, YAML, and TOML files, along with existing sources.
        """
        return (
            JsonConfigSettingsSource(settings_cls, "eolic.json"),
            YamlConfigSettingsSource(settings_cls, "eolic.yaml"),
            TomlConfigSettingsSource(settings_cls, "eolic.toml"),
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )
