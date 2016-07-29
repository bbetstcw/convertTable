任务 | 服务管理模式 | 资源管理器模式
-------------- | ----------- | -------------------------
创建最基本的 VM | `azure vm create [options] <dns-name> <image> [userName] [password]` | `azure vm quick-create [options] <resource-group> <name> <location> <os-type> <image-urn> <admin-username> <admin-password>`<br/><br/>（从 `azure vm image list` 命令获取 `image-urn`。有关示例，请参阅 [Windows](/documentation/articles/virtual-machines-windows-cli-ps-findimage) 或者 [Linux](/documentation/articles/virtual-machines-linux-cli-ps-findimage)。）
创建 Linux VM | `azure vm create [options] <dns-name> <image> [userName] [password]` | `azure  vm create [options] <resource-group> <name> <location> -y "Linux"`
创建 Windows VM | `azure vm create [options] <dns-name> <image> [userName] [password]` | `azure  vm create [options] <resource-group> <name> <location> -y "Windows"`
列出 VM | `azure  vm list [options]` | `azure  vm list [options]`
获取有关 VM 的信息 | `azure  vm show [options] <vm_name>` | `azure  vm show [options] <resource_group> <name>`
启动 VM | `azure vm start [options] <name>` | `azure vm start [options] <resource_group> <name>`
停止 VM | `azure vm shutdown [options] <name>` | `azure vm stop [options] <resource_group> <name>`
释放 VM | 不可用 | `azure vm deallocate [options] <resource-group> <name>`
重新启动 VM | `azure vm restart [options] <vname>` | `azure vm restart [options] <resource_group> <name>`
删除 VM | `azure vm delete [options] <name>` | `azure vm delete [options] <resource_group> <name>`
捕获 VM | `azure vm capture [options] <name>` | `azure vm capture [options] <resource_group> <name>`
从用户映像创建 VM | `azure  vm create [options] <dns-name> <image> [userName] [password]` | `azure  vm create [options] -q <image-name> <resource-group> <name> <location> <os-type>`
从专用磁盘创建 VM | `azure  vm create [options]-d <custom-data-file> <dns-name> [userName] [password]` | `azue  vm create [options] -d <os-disk-vhd> <resource-group> <name> <location> <os-type>`
将数据磁盘添加到 VM | `azure  vm disk attach [options] <vm-name> <disk-image-name>` -或- <br/> `vm disk attach-new [options] <vm-name> <size-in-gb> [blob-url]` | `azure  vm disk attach-new [options] <resource-group> <vm-name> <size-in-gb> [vhd-name]`
从 VM 中删除数据磁盘 | `azure  vm disk detach [options] <vm-name> <lun>` | `azure  vm disk detach [options] <resource-group> <vm-name> <lun>`
将泛型扩展添加到 VM | `azure  vm extension set [options] <vm-name> <extension-name> <publisher-name> <version>` | `azure  vm extension set [options] <resource-group> <vm-name> <name> <publisher-name> <version>`
将 VM 访问扩展添加到 VM | 不可用 | `azure vm reset-access [options] <resource-group> <name>`
将 Docker 扩展添加到 VM | `azure  vm docker create [options] <dns-name> <image> <user-name> [password]` | `azure  vm docker create [options] <resource-group> <name> <location> <os-type>`
将 Chef 扩展添加到 VM | `azure  vm extension get-chef [options] <vm-name>` | 不可用
禁用 VM 扩展 | `azure  vm extension set [options] -b <vm-name> <extension-name> <publisher-name> <version>` | 不可用
删除 VM 扩展 | `azure  vm extension set [options] -u <vm-name> <extension-name> <publisher-name> <version>` | `azure  vm extension set [options] -u <resource-group> <vm-name> <name> <publisher-name> <version>`
列出 VM 扩展 | `azure vm extension list [options]` | 不可用
显示 VM 映像 | `azure vm image show [options]` | 不可用
获取 VM 资源的使用情况 | 不可用 | `azure vm list-usage [options] <location>`
获取所有可用 VM 大小 | 不可用 | `azure vm sizes [options]`