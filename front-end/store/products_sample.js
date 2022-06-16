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
        price: 100
      },
      {
        id: 2,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      },
      {
        id: 3,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      },
      {
        id: 4,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      },
      {
        id: 5,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      },
      {
        id: 6,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      },
      {
        id: 7,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      },
      {
        id: 8,
        Name: 'Yerba',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      },
      {
        id: 9,
        Name: 'Pollo',
        Brand: 'Marca',
        UrlImg: 'https://picsum.photos/200',
        description: '1kg',
        update_at: '12/7/22',
        price: 100
      }
    ]
  })
});

// async fetch() {
//   this.products = await fetch(
//     'http://www.ahorrapp.me/api/product/1'
//   ).then(res => res.json())
// }
