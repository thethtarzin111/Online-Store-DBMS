PGDMP      /                |            store4    16.2    16.2      6           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            7           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            8           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            9           1262    16491    store4    DATABASE     h   CREATE DATABASE store4 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE store4;
                postgres    false            �            1259    16493    customer    TABLE     =  CREATE TABLE public.customer (
    "CustomerID" integer NOT NULL,
    "CustomerFirstName" character varying NOT NULL,
    "CustomerLastName" character varying NOT NULL,
    "CustomerPhoneNumber" character varying NOT NULL,
    "CustomerStreetAddress" character varying,
    "CustomerCityAddress" character varying
);
    DROP TABLE public.customer;
       public         heap    postgres    false            �            1259    16498    order    TABLE     |   CREATE TABLE public."order" (
    orderid integer NOT NULL,
    customerid integer NOT NULL,
    orderdate date NOT NULL
);
    DROP TABLE public."order";
       public         heap    postgres    false            �            1259    16503    product    TABLE     �   CREATE TABLE public.product (
    productid character varying NOT NULL,
    productname character varying NOT NULL,
    price numeric NOT NULL,
    warehouseid integer,
    amountofproduct integer
);
    DROP TABLE public.product;
       public         heap    postgres    false            �            1259    16662    productorder    TABLE     �   CREATE TABLE public.productorder (
    orderid integer NOT NULL,
    productid character varying NOT NULL,
    "productAmount" integer
);
     DROP TABLE public.productorder;
       public         heap    postgres    false            �            1259    16508    supplier    TABLE     �   CREATE TABLE public.supplier (
    "SupplierID" integer NOT NULL,
    "SupplierName" character varying NOT NULL,
    "ProductID" character varying NOT NULL,
    "SupplierContactNumber" character varying NOT NULL
);
    DROP TABLE public.supplier;
       public         heap    postgres    false            �            1259    16513    transaction    TABLE     
  CREATE TABLE public.transaction (
    "TransactionID" integer NOT NULL,
    "CustomerID" integer NOT NULL,
    "OrderID" integer NOT NULL,
    "TotalSumOfOrder" integer NOT NULL,
    "TransactionDate" date NOT NULL,
    "PaymentMethod" character varying NOT NULL
);
    DROP TABLE public.transaction;
       public         heap    postgres    false            �            1259    16518 	   warehouse    TABLE     l   CREATE TABLE public.warehouse (
    "WarehouseID" integer NOT NULL,
    warehouse_city character varying
);
    DROP TABLE public.warehouse;
       public         heap    postgres    false            -          0    16493    customer 
   TABLE DATA           �   COPY public.customer ("CustomerID", "CustomerFirstName", "CustomerLastName", "CustomerPhoneNumber", "CustomerStreetAddress", "CustomerCityAddress") FROM stdin;
    public          postgres    false    215   $&       .          0    16498    order 
   TABLE DATA           A   COPY public."order" (orderid, customerid, orderdate) FROM stdin;
    public          postgres    false    216   �&       /          0    16503    product 
   TABLE DATA           ^   COPY public.product (productid, productname, price, warehouseid, amountofproduct) FROM stdin;
    public          postgres    false    217   �&       3          0    16662    productorder 
   TABLE DATA           K   COPY public.productorder (orderid, productid, "productAmount") FROM stdin;
    public          postgres    false    221   r(       0          0    16508    supplier 
   TABLE DATA           f   COPY public.supplier ("SupplierID", "SupplierName", "ProductID", "SupplierContactNumber") FROM stdin;
    public          postgres    false    218   �(       1          0    16513    transaction 
   TABLE DATA           �   COPY public.transaction ("TransactionID", "CustomerID", "OrderID", "TotalSumOfOrder", "TransactionDate", "PaymentMethod") FROM stdin;
    public          postgres    false    219    *       2          0    16518 	   warehouse 
   TABLE DATA           B   COPY public.warehouse ("WarehouseID", warehouse_city) FROM stdin;
    public          postgres    false    220   =*       �           2606    16524    customer Customer_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT "Customer_pkey" PRIMARY KEY ("CustomerID");
 B   ALTER TABLE ONLY public.customer DROP CONSTRAINT "Customer_pkey";
       public            postgres    false    215            �           2606    16526    order OrderID 
   CONSTRAINT     T   ALTER TABLE ONLY public."order"
    ADD CONSTRAINT "OrderID" PRIMARY KEY (orderid);
 ;   ALTER TABLE ONLY public."order" DROP CONSTRAINT "OrderID";
       public            postgres    false    216            �           2606    16528    product Product_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.product
    ADD CONSTRAINT "Product_pkey" PRIMARY KEY (productid);
 @   ALTER TABLE ONLY public.product DROP CONSTRAINT "Product_pkey";
       public            postgres    false    217            �           2606    16530    supplier Supplier_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT "Supplier_pkey" PRIMARY KEY ("SupplierID");
 B   ALTER TABLE ONLY public.supplier DROP CONSTRAINT "Supplier_pkey";
       public            postgres    false    218            �           2606    16532    transaction TransactionID 
   CONSTRAINT     f   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT "TransactionID" PRIMARY KEY ("TransactionID");
 E   ALTER TABLE ONLY public.transaction DROP CONSTRAINT "TransactionID";
       public            postgres    false    219            �           2606    16534    warehouse Warehouse_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.warehouse
    ADD CONSTRAINT "Warehouse_pkey" PRIMARY KEY ("WarehouseID");
 D   ALTER TABLE ONLY public.warehouse DROP CONSTRAINT "Warehouse_pkey";
       public            postgres    false    220            �           1259    16695    idx_order_date    INDEX     G   CREATE INDEX idx_order_date ON public."order" USING btree (orderdate);
 "   DROP INDEX public.idx_order_date;
       public            postgres    false    216            �           2606    16535    order CustomerID    FK CONSTRAINT     �   ALTER TABLE ONLY public."order"
    ADD CONSTRAINT "CustomerID" FOREIGN KEY (customerid) REFERENCES public.customer("CustomerID");
 >   ALTER TABLE ONLY public."order" DROP CONSTRAINT "CustomerID";
       public          postgres    false    215    216    3467            �           2606    16540    transaction CustomerID    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT "CustomerID" FOREIGN KEY ("CustomerID") REFERENCES public.customer("CustomerID") NOT VALID;
 B   ALTER TABLE ONLY public.transaction DROP CONSTRAINT "CustomerID";
       public          postgres    false    215    219    3467            �           2606    16545    transaction OrderID    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT "OrderID" FOREIGN KEY ("OrderID") REFERENCES public."order"(orderid) NOT VALID;
 ?   ALTER TABLE ONLY public.transaction DROP CONSTRAINT "OrderID";
       public          postgres    false    219    3469    216            �           2606    16550    supplier ProductID    FK CONSTRAINT     �   ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT "ProductID" FOREIGN KEY ("ProductID") REFERENCES public.product(productid) NOT VALID;
 >   ALTER TABLE ONLY public.supplier DROP CONSTRAINT "ProductID";
       public          postgres    false    218    217    3472            �           2606    16560    product WarehouseID    FK CONSTRAINT     �   ALTER TABLE ONLY public.product
    ADD CONSTRAINT "WarehouseID" FOREIGN KEY (warehouseid) REFERENCES public.warehouse("WarehouseID") NOT VALID;
 ?   ALTER TABLE ONLY public.product DROP CONSTRAINT "WarehouseID";
       public          postgres    false    220    3478    217            �           2606    16673    productorder fk_order    FK CONSTRAINT     {   ALTER TABLE ONLY public.productorder
    ADD CONSTRAINT fk_order FOREIGN KEY (orderid) REFERENCES public."order"(orderid);
 ?   ALTER TABLE ONLY public.productorder DROP CONSTRAINT fk_order;
       public          postgres    false    221    216    3469            �           2606    16690    productorder fk_product    FK CONSTRAINT     �   ALTER TABLE ONLY public.productorder
    ADD CONSTRAINT fk_product FOREIGN KEY (productid) REFERENCES public.product(productid) NOT VALID;
 A   ALTER TABLE ONLY public.productorder DROP CONSTRAINT fk_product;
       public          postgres    false    217    221    3472            -   l   x�3��M,��t*�/��424�52�Ե022��I-(8���4?/;��T�Ѐ�#5�83/;�ˈ�+?#�ӱ� '����X���Ȑ32'3� ����Ȃ�'1�$�+F��� ���      .   9   x�U˱  �:�%(vB�.�?T���*��Py�k���A0ʿ��]f/� p ��      /   y  x����n�0F���� cl�᧤�6E�ګ���4A5feX�ҧ�I�Bӕ6�>���7�=�d�<N�Y�c�-�=5��0�"��{/�
.$䖰opjNdY�樉hmg�#�'
62�"���C�����9���e�u�&v�	�Րm^��
J��_gVj�?��.��_�ی	�;�Clk^]*W�U^�R�cCh�l�7b��#�rFۺ�RPh:�i�u���H�ʠ.�-�e���T�{V]%Kb�]��~��'�;�R���8�g��[�N�?^�����
�=ڞZ��{Y��U���2�r�-��Y;�Xt��Z�)uK��a�w���
��ЏB�أ�����\��K^OD+Hr���<����g      3   8   x�342��u�455���2��Px@9c.#c0�(f�1��300�4����� ��$      0   V  x�m��n�0@��+<���`C24��*�2uA�X%��D�s2t�����BB�=�ɴ=ˮ�xs,V��֋dOZ�g&È+'�"�j&����8b��#:H�\�j"�y��7^�����f�L3]M�H:�_Z��ة� �{����,�k&3X���}���8i�{���Ѳ�#7��Pm3!7�B��dH��ph	;��K�9x��T����	=�@=8d��w�n;�à.�4�s�NB�5�8�L͙�Й�uP��I��V�@1"��ˌfb��������Xx��k� ���f�c?q���,�:Zj���UJ(Zw�1�7��~����a�@G�䊖�c�/���9      1      x������ � �      2   ;   x��0�402��I,(HM�+J�+I�2316�0��H�)�����2777��(������ ���     