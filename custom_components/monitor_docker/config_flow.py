from homeassistant import config_entries
from homeassistant.core import HomeAssistant
import voluptuous as vol
from .const import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class DockerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Docker Monitor."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Validate the user input here
            return self.async_create_entry(title="Docker Monitor", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("name"): str,
                vol.Required("retry"): int,
            }),
            errors=errors,
        )