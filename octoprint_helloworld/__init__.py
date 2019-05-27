# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.wikipedia.org/wiki/Hello_world",
                    something="This is important")

	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/helloworld.js"],
			css=["css/helloworld.css"],
			less=["less/helloworld.less"]
		)

    ##~~ SettingsPlugin
	def get_settings_defaults(self):
		return dict(command="",
			stored_mesh=[],
			stored_mesh_x=[],
			stored_mesh_y=[],
			stored_mesh_z_height=2,
			save_mesh=True,
			mesh_timestamp="",
			flipX=False,
			flipY=False,
			stripFirst=False,
			use_center_origin=False,
			use_relative_offsets=False,
			timeout=60)

__plugin_name__ = "Hello World"
__plugin_implementation__ = HelloWorldPlugin()
