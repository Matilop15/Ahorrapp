import { defineStore } from 'pinia';

export const useProductsSampleStore = defineStore('products_sample', {
  state: () => ({
    products_sample: [
      {
        id: 1,
        Name: 'Arroz',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'Ta-ta'
      },
      {
        id: 2,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'Disco'
      },
      {
        id: 3,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'Geant'
      },
      {
        id: 4,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'Los Paraisos'
      },
      {
        id: 5,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'Mastilazo'
      },
      {
        id: 6,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'Lo de pepe'
      },
      {
        id: 7,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'Fiumba Market'
      },
      {
        id: 8,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'a Market'
      },
      {
        id: 9,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100,
        market: 'coso Market'
      }
    ]
  })
});

// async fetch() {
//   this.products = await fetch(
//     'http://www.ahorrapp.me/api/product/1'
//   ).then(res => res.json())
// }
