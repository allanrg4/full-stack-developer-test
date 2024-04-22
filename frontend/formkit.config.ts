import { defineFormKitConfig } from '@formkit/vue'
import { es } from '@formkit/i18n'
import { genesisIcons } from '@formkit/icons'

import { rootClasses } from './formkit.theme'

export default defineFormKitConfig({
  locale: 'es',
  locales: { es },
  config: { rootClasses },
  icons: { ...genesisIcons },
})
