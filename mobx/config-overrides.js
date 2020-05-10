const { addDecoratorsLegacy, useEslintRc, override, addBundleVisualizer } = require('customize-cra')

module.exports = override(
  addDecoratorsLegacy(),
  useEslintRc('./.eslintrc'),

  addBundleVisualizer({}, true)
)
