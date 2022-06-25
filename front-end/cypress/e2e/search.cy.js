describe('Search Item', () => {
  it('Search a product', () => {
    cy.visit('/')

    .get('input#search-bar').click()
      .type('har')
    .get('#description > div > h3').first()
      .contains('har', { matchCase: false })
  })
})