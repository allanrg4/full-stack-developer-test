import { defineFormKitConfig } from '@formkit/vue'
import { genesisIcons } from '@formkit/icons'

import { rootClasses } from './formkit.theme'

export default defineFormKitConfig({
  config: {
    rootClasses,
  },
  icons: { ...genesisIcons },
})
