package datadog

valid_container(c) {
	c.inspect.HostConfig.CgroupParent == ""
}
